// ent useage

// count
// app.EntClient.UserBookCompressedItems.Query().Where(
//         sUserBookCompressedItems.UserID(userID),
//         sUserBookCompressedItems.BookID(bookID),
//     ).Count(ctx)

// get
// app.EntClient.UserBookCompressedItems.Query().Where(
//         sUserBookCompressedItems.UserID(userID),
//         sUserBookCompressedItems.BookID(bookID),
//     ).First(ctx)

// delete
// app.EntClient.UserBookCompressedItems.Delete().Where(
//         sUserBookCompressedItems.UserID(userID),
//         sUserBookCompressedItems.BookID(bookID),
//     ).Exec(ctx)
